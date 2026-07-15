"""
LeetCode 355. Design Twitter

Topic:
- Design
- Heap
- Hash Map
- Set

Pattern:
- K-Way Merge with Min Heap

Idea:
Store each user's tweets in chronological order.

Each tweet stores:

(count, tweetId)

Use a decreasing count as the timestamp:

0, -1, -2, -3, ...

Since Python provides a min heap, the newest tweet
has the smallest count and will be popped first.

To generate the news feed:

1. Add the user to their own follow set so they
   can see their own tweets.
2. For every followed user:
   - Get their most recent tweet.
   - Push it into the min heap.
3. Pop the globally newest tweet.
4. Add its tweetId to the result.
5. Push the same user's next older tweet
   into the heap.
6. Stop after collecting 10 tweets or when
   the heap becomes empty.

Each heap element stores:

(count, tweetId, followeeId, previous_index)

Remember:

Get Latest Tweet from Each Followed User

↓

Push into Min Heap

↓

Pop Globally Newest Tweet

↓

Add Tweet to Result

↓

Push Same User's Previous Tweet

↓

Repeat Until 10 Tweets

Time Complexity:

postTweet: O(1)

follow: O(1)

unfollow: O(1)

getNewsFeed: O(F + 10 log F)

Space Complexity: O(F)

where F is the number of followed users.

The heap contains at most one tweet from each
followed user at a time.
"""


from collections import defaultdict
from typing import List
import heapq


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # The user should be able to see their own tweets.
        self.followMap[userId].add(userId)

        # Add the latest tweet from every followed user.
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1

                count, tweetId = self.tweetMap[followeeId][index]

                minHeap.append([
                    count,
                    tweetId,
                    followeeId,
                    index - 1
                ])

        heapq.heapify(minHeap)

        # Merge the tweet lists and collect at most 10 tweets.
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = (
                heapq.heappop(minHeap)
            )

            res.append(tweetId)

            # Push the same user's next older tweet.
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]

                heapq.heappush(
                    minHeap,
                    [
                        count,
                        tweetId,
                        followeeId,
                        index - 1
                    ]
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


if __name__ == "__main__":
    twitter = Twitter()

    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))  # [5]

    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))  # [6, 5]

    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))  # [5]
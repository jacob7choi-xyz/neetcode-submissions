class Twitter:

    def __init__(self):
        self.tweet = {}
        self.following = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if userId not in self.tweet:
            self.tweet[userId] = []
        self.tweet[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following.get(userId, set()) | {userId} 
        heap = []
        for user in users:
            for timestamp, tweetId in self.tweet.get(user,[]):
                heap.append((-timestamp, tweetId))
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            _, tweets = heapq.heappop(heap)
            feed.append(tweets)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
       

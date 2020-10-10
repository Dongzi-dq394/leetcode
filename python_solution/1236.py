# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # Solution by myself: BFS + Queue (204ms: 94.93%)
        def judge(url1, url2):
            return url1[7:].split('/')[0]==url2[7:].split('/')[0]
        visited = {startUrl: True}
        queue = deque([startUrl])
        res = []
        while queue:
            URL = queue.popleft()
            res.append(URL)
            for sub_url in htmlParser.getUrls(URL):
                if sub_url not in visited and judge(startUrl, sub_url):
                    visited[sub_url] = True
                    queue.append(sub_url)
        return res
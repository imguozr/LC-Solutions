from typing import List


class Solution:
    """
        DFS.
        https://mp.weixin.qq.com/s/Y7snQIraCC6PRhj9ZSnlzw
    """

    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        origin_color = image[sr][sc]
        self.fill(image, sr, sc, origin_color, new_color)
        return image

    def fill(self, image, x, y, origin, new):
        if not (0 <= x < len(image) and 0 <= y < len(image[0])):
            return
        if image[x][y] != origin:
            return
        if image[x][y] == -1:
            return

        image[x][y] = -1
        self.fill(image, x - 1, y, origin, new)
        self.fill(image, x + 1, y, origin, new)
        self.fill(image, x, y - 1, origin, new)
        self.fill(image, x, y + 1, origin, new)
        image[x][y] = new

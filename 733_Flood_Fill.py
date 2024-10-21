from typing import List
def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        
        def traverse(origin, sr, sc, color):
            if sr < 0 or sc < 0 or sr >= m or sc >= n:
                return 
            if image[sr][sc] == color or image[sr][sc] != origin:
                return
            image[sr][sc] = color

            traverse(origin, sr - 1, sc, color)
            traverse(origin, sr + 1, sc, color)
            traverse(origin, sr, sc - 1, color)
            traverse(origin, sr, sc + 1, color)
       
        traverse(image[sr][sc], sr, sc, color)    
        return image


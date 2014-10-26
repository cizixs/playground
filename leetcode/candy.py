class Candy:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candys = [1] * len(ratings)

        for i in range(len(ratings)):
            if i > 0 and ratings[i] > ratings[i-1]:
                candys[i] = candys[i-1] + 1

        j = len(ratings)-2
        while j >= 0:
            if ratings[j] > ratings[j+1]:
                candys[j] = max(candys[j], candys[j+1]+1)
            j -= 1

        return sum(candys)

if __name__ == "__main__":
    ratings = [2,1]
    print(Candy().candy(ratings))

# def current_beat():
# 	nums = (1, 2, 3, 4)
# 	i = 0
# 	while True:
# 		if i >= len(nums): i = 0
# 		yield nums[i]
# 		i+=1

# count = current_beat()
# print(next(count))
# print(next(count))
# print(next(count))
# print(next(count))
# print(next(count))

def make_song(count = 99, bev = "soda"):
	while count >= 0:
		if count == 0:
			yield "No more {}!".format(bev)
			break
		elif count == 1:
			yield "Only 1 bottle of {} left!".format(bev)
			count-=1
		else:
			yield "{} bottles of {} on the wall.".format(count, bev)
			count-=1



song = make_song()
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
        
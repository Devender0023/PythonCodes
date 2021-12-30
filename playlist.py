playlist =  {
	'title':'playlist1',
	'author': 'Dev',
	'songs': [
		{'name' : 'song1','singers' : ['one'],'duration': 2.5},
		{'name' : 'song2','singers' : ['two'],'duration': 3},
		{'name' : 'song3','singers' : ['two', 'three'],'duration': 1.4}
	]
}
total_duration = 0
for song in playlist['songs']:
	total_duration += song['duration']

print(total_duration)
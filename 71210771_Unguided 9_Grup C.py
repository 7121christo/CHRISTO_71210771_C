class PriorityQueueSortedList :
	def __init__(self) :
		self._data = []
		self._size = 0
	
	def add(self, data, priority) :
		data = [int(priority), data]
		self._data.append(data)
		self._data.sort()
		self._size += 1
	
	def is_empty(self):
		if self._size == 0:
			return True
		else:
			return False

	def __len__(self):
		return self._size

	def remove(self) :
		del self._data[0]
		self._size -= 1
	
	def peek(self) :
		print("Data prioritas tertinggi:", tuple(self._data[0][::-1]))
	
	def removePriority(self, n) :
		lst2 = []
		for x in range(len(self._data)) :
			if self._data[x][0] == n :
				del self._data[x][1]
		for y in range(len(self._data)) :
			if len(self._data[y]) == 1 :
				pass
			else :
				lst2.append(self._data[y])
		self._data = lst2
		self._size -= 1
	
	def printIsiQueue(self) :
		if self._size == 0 :
			print("Priority Queue Kosong")
		count = 0
		print("Isi Semua Queue", end = ": ")
		for x in self._data :
			count += 1
			if count < len(self._data) :
				print(tuple(x[::-1]), end = ", ")
			elif count == len(self._data) :
				print(tuple(x[::-1]))

	def update(self, prioBaru, dataBaru):
		if self.is_empty() is True:
			print("Priority Queue Kosong")
		else:
			lst3 = []
			for i in range(len(self._data)):
				if self._data[i][1] == prioBaru:
					self._data[i] = (dataBaru, prioBaru)


sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printIsiQueue()
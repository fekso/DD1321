from linkedQFile import LinkedQ
li = [7,1,12,2,8,3,11,4,9,5,13,6,10]

q = LinkedQ()
for number in li:
    q.enqueue(number)
D1list = []

while q.isEmpty() == False:
    x = q.dequeue()
    q.enqueue(x)
    y = q.dequeue()
    D1list.append(y)

print("I rätt ordning: ", D1list)

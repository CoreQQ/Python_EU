import asyncio
from time import time

#waiting 2 seconds. print text
async def tabs():
    await asyncio.sleep(2)
    print(" ")

#Print text. Waiting paid (5sec). Print text
async def buyer1():
    print("Buyer1 Scanned the item...")
    await asyncio.sleep(5)
    print("Bayer1 paid for the item")
    
#Print text. Waiting paid (6.5sec). Print text    
async def buyer2():
    print("Buyer2 Scanned the item...")
    await asyncio.sleep(6.5)
    print("Bayer2 paid for the item")
    
#Print text. Waiting paid (6sec). Print text
async def buyer3():
    print("Buyer3 Scanned the item...")
    await asyncio.sleep(6)
    print("Bayer3 paid for the item")
    
#Print text. Waiting paid (5sec). Print text    
async def buyer4():
    print("Buyer4 Scanned the item...")
    await asyncio.sleep(5)
    print("Bayer4 paid for the item")
    

#Create 5 tasks, add to loop task. 
async def main():
    task1 = asyncio.create_task(buyer1())
    task2 = asyncio.create_task(buyer2())
    task3 = asyncio.create_task(buyer3())
    task4 = asyncio.create_task(buyer4())
    tab = asyncio.create_task(tabs())
    
    await asyncio.gather(task1, task2, task3, task4, tab)


#Start async main function
if __name__ == "__main__":
    asyncio.run(main())
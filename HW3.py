import random

page_table = {}
secondary_disk = []
offset_size = 256 #256 corresponds to 2 hex digits
number_of_pages = 16 #number of pages in logical memory
number_of_frames = 8 #number of frames in physical memory
created_frames = 0 #holds how many frames have been made (so more aren't made than are aviable)

def swap_in(page_in): #swaps in a page from secondary_disk to page_table when no more frames can be created
	page_out = random.choice(list(page_table.keys())) #finds a random page to remove from the page table
	frame_num = page_table[page_out] #get its frame
	page_table.pop(page_out) #removes the page from the page_table
	page_table[page_in] = frame_num #adds the new page to the page_table with the frame number from the old page
	secondary_disk.remove(page_in) #remove the page number that just got added to the page table from the secondary disk
	return frame_num


def translate(log_addr): #gives a physical address from a given logical address
	global created_frames #python syntax thing
	#bt = base ten
	bt_log_addr = int(log_addr, 16) #get the base ten version of the logical address for operations
	if bt_log_addr < 0 or bt_log_addr >= number_of_pages * offset_size:
		raise Exception(f"Logical address 0x{log_addr} is not within logcial address space")
	bt_page_num = int(bt_log_addr / offset_size) #finds how many offsets are in this logical address to give page number
	bt_offset = bt_log_addr % offset_size #finds remaining bytes left to traverse after getting to the page number
	
	page_num = hex(bt_page_num).replace("0x","").upper() #hex page num
	offset = hex(bt_offset).replace("0x","").upper() #hex offset
	
	
	if page_num in page_table.keys(): #if the page is already in the page table
		frame_num = page_table[page_num] #use the page table
	elif page_num in secondary_disk and created_frames < number_of_frames: #if the page isn't in the page table, but there are frames left to assing
		frame_num = hex(created_frames).replace("0x","").upper() #create the next frame
		created_frames += 1
		page_table[page_num] = frame_num #map the page number to the frame
		secondary_disk.remove(page_num) #remove the page from the disk
	elif page_num in secondary_disk: #if the page is not in the page table and there is no frames available
		frame_num = swap_in(page_num) #swap this page number into the page_table by removeing a random page
	else: #if none of the above happen
		raise Exception(f"Page number {page_num} is not in memory")
		
	bt_frame_num = int(frame_num, 16) #base ten of the frame found earlier
	bt_phy_addr = (bt_frame_num * offset_size) + bt_offset #finds physical address
	phy_addr = hex(bt_phy_addr).replace("0x","").upper() #hex of physical address
	
	#list formatting for printing later
	translate_data = []
	translate_data.append(log_addr)
	translate_data.append(page_num)
	translate_data.append(offset)
	translate_data.append(phy_addr)
	translate_data.append(frame_num)
	translate_data.append(offset)
	return translate_data
	
def print_translate_data(data, run): #prints the logical and physical address
	#balances the sizes of the physical and logical address in case there were some zeroes (just to look better when printing)
	if len(data[0]) < len(data[3]):
		diff = len(data[3]) - len(data[0])
		for _ in range(0, diff):
			data[0] = "0" + data[0]
	elif len(data[3]) < len(data[0]):
		diff = len(data[0]) - len(data[3])
		for _ in range(0, diff):
			data[3] = "0" + data[3]
	#print
	print(f"Run {run}:")
	print(f"\tLogical Address: 0x{data[0]}")
	print(f"\tPage Number: 0x{data[1]}")
	print(f"\tOffset: 0x{data[2]}")
	print("\t-->")
	print(f"\tPhysical Address: 0x{data[3]}")
	print(f"\tFrame Number: 0x{data[4]}")
	print(f"\tOffset: 0x{data[5]}")


def gen_log_addr(): #gernates a logical address from the logical address space
    return hex(random.randrange(0, number_of_pages * offset_size)).replace("0x","").upper() #number of pages * offset size = number of bytes in logical address space

def initlize_pages_to_disk(): # adds all pages to the secondary disk to start
	for x in range(0, number_of_pages):
		secondary_disk.append(hex(x).replace("0x","").upper())

initlize_pages_to_disk()

for x in range(0,10): #translate 10 addressess
	log_addr = gen_log_addr()
	translate_data = translate(log_addr)
	print_translate_data(translate_data, x)
print("Page table at end\n", page_table)
print("Secondary disk at end\n", secondary_disk)




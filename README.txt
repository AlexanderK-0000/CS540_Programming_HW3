There is two files in here.

HW3.cpp is a c++ file that is *based on what the proffesor uploaded to blackboard
	*It basically just is what he uploaded to blackboard; I only made small changes (he just kind of gave us the answer, I think?)
	This one maps page numbers to frame numbers by modding the page number to be within the frame number
	
HW3.py is a python file that I wrote. It does a simalar thing to the c++ file, but includes a "secondary disk"
	Maps page numbers as they are called to frame numbers sequtionely until all frame numbers are used
	After that, pages are swapped into the page table from disk by removing a random page from the table and linking the new page to its frame number
	This is to try to emulate demand paging
	Tried to make an effort to do something since the cpp file was just given to us, and I felt kind of bad about it
	
Also, I used the offset size of 256 for each file. That's represented with 8 bits and therefore correpsonds cleanly to 2 hex digits
The 1024 offset size the cpp file from the proffesor orginally used was represented with 10 bits (2.5 hex digits) which was just incredibly confusing to look at
Though, both files should theorectially work with any offset size, number of pages, and number of frames.

The c++ file can be ran at: https://www.onlinegdb.com/online_c++_compiler
The pyhton file can be ran at: https://www.onlinegdb.com/online_python_compiler

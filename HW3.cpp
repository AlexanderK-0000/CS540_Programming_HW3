//  Note: Code in C++
//  Note: The code simulates address translation between logical and physical memory in a virtual memory system, displaying both logical and physical addresses in hexadecimal format.

#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <iomanip> // For std::hex

using namespace std;

const int PAGE_SIZE = 256;  // Page size in bytes (2^8 = 256; meaning 8 bits are used for the offset [2 hex digits])
const int FRAME_SIZE = 256; // Frame size in bytes (2^10 = 256; meaning 8 bits are used for the offset [2 hex digits])
const int NUM_PAGES = 16;    // Number of pages in logical memory
const int NUM_FRAMES = 8;    // Number of frames in physical memory

// Function to generate a random logical address
int generateLogicalAddress() {
    return rand() % (NUM_PAGES * PAGE_SIZE); // Generates a random logical address within the range of logical memory
}

int main() {
    srand(time(nullptr)); // Seed random number generator with current time

    // Initialize page/frame table
    vector<int> pageFrameTable(NUM_PAGES, -1); // Page/frame table initialized with -1 indicating no mapping initially

    // Allocate frames in physical memory
    vector<int> physicalMemory(NUM_FRAMES, -1); // Physical memory initialized with -1 indicating empty frames initially

    // Fill page/frame table and physical memory
    for (int i = 0; i < NUM_PAGES; ++i) {
        pageFrameTable[i] = i % NUM_FRAMES; // Circular mapping of pages to frames ensures each page has a corresponding frame
    }

    // Generate logical addresses and translate them into physical addresses
    // This loop translates 10 random logical addresses to physical addresses using the page/frame table
    for (int i = 0; i < 10; ++i) {
        int logicalAddress = generateLogicalAddress(); // Generates a random logical address
        int pageNumber = logicalAddress / PAGE_SIZE; // Calculates the page number from the logical address
        int offset = logicalAddress % PAGE_SIZE; // Calculates the offset within the page from the logical address

        if (pageNumber < NUM_PAGES) { // Check if the page number is within the valid range
            int frameNumber = pageFrameTable[pageNumber]; // Retrieves the frame number corresponding to the page from the page/frame table
            int physicalAddress = frameNumber * FRAME_SIZE + offset; // Calculates the physical address by adding offset to the base address of the frame
            
            
            cout << "Run " << i <<"\n\tLogical Address: 0x" << hex << logicalAddress << "\n\tPage Number: 0x" << pageNumber << "\n\tBase Page Address: 0x"<< pageNumber*PAGE_SIZE << "\n\tOffset: 0x" << offset << "\n\t=>\n\tPhysical Address: 0x" << physicalAddress << "\n\tFrame Number: 0x" << frameNumber << "\n\tBase Frame Address: 0x"<< frameNumber*FRAME_SIZE << "\n\tOffset: 0x" << offset << endl; // Prints the logical and physical addresses in hexadecimal format
        } 
        else {
            cout << "Invalid Page Number: " << pageNumber << endl; // Prints an error message for invalid page number
        }
    }

    return 0;
}

import hashlib
import math
import time

def find_difficulty(target):
    thetarget=int(prefix+target,16)
    difficulty_bits=256-math.log(thetarget,2)
    difficulty=2**difficulty_bits
    print("============================================================================================================= \n")
    print("Target: \t %s" % (target))
    print("Difficulty: \t %d " % (difficulty))
    return


def find_nonce(header,target):
    thetarget=int(prefix+target,16)
    for nonce in range(max_nonce):
        hash_result = hashlib.sha256(str(header).encode()+str(nonce).encode()).hexdigest()
        if int(hash_result,16) < thetarget:
            print("Hash: \t \t %s " % hash_result)
            print("Nonce: \t \t %s" % hex(nonce))
            print("Hash Attempts: \t %d" % nonce)
            return(hash_result,nonce)

    print("Failed to find nonce");




if __name__ == '__main__':
    target_list=["00ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
    "0000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"]
    prefix="0x"
    max_nonce=2**32
    header="message".encode()
    for target in target_list:
        find_difficulty(target)
        start_time = time.clock()
        find_nonce(header,target)
        print("Time Elapsed: \t %s seconds \n" % (time.clock() - start_time))


    print("=============================================================================================================")

    print("\n We find the time and space complexity for finding the right hash increases exponentially with decrease in target values \n")
    print("=============================================================================================================")
    print("\n A 32 bit nonce may not always be enough to find the right hash. We have 2^32 different hash attempts which is around 4 billion tries. \n For eg: if target has 9 leading zeroes, then the probability of finding the right hash is nearly zero. ")
    print("\n=============================================================================================================")

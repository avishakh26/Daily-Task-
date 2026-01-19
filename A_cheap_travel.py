


# n = total travel
# m = ride coverd by one special ticket

n,m,a,b = map(int,input().split())


onetime_tic = n*a



full_tic = n//m       # after that we get m*ans rides ticket

ride = n % m    # how many rides are still left



final = full_tic*b + min( ride*a,b)             #cost of full mtic + cheapest way

answer = min(final,onetime_tic) 

print(answer)



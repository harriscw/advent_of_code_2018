rm(list=ls())
input=as.numeric(readLines("../input.txt"))

paste("Part 1:",sum(input))

ind=1
acc=0
seen=c()
whilecnt=1
start=Sys.time()
while(TRUE){
  acc=acc+input[ind]

  if(!(acc %in% seen)){
    seen=c(seen,acc)
  }else{
    print(paste("Part 2:",acc,round(difftime(Sys.time(),start,units="mins"),2),"min"))
    break
  }
  
  ind=ind+1
  if(ind>length(input)){
    whilecnt=whilecnt+1
    if(whilecnt %% 10==0){print(whilecnt)}
    ind=1
  }
}
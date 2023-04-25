rm(list=ls())
input=as.numeric(readLines("../input.txt"))

paste("Part 1:",sum(input))

ind=1
acc=0
seen=c()
whilecnt=1
start=Sys.time()
thelength=length(input)
while(TRUE){
  acc=acc+input[ind]

  if(!(acc %in% seen)){
    seen=c(seen,acc)
  }else{
    print(paste("Part 2:",acc,round(difftime(Sys.time(),start,units="mins"),2),"min"))
    break
  }
  
  ind=ind+1
  if(ind>thelength){
    whilecnt=whilecnt+1
    if(whilecnt %% 10==0){print(whilecnt)}
    ind=1
  }
}

###
# Make some plots
###

library(lattice)

mat=matrix(0,500,500) #initialize a 500x500 matrix of 0s
cnt=1
plotnum=1
for(thisnum in seen){
  row=floor(thisnum/500)+1 #every 500 start a new row
  col=thisnum-500*floor(thisnum/500)+1 #take row out to get column
  
  mat[row,col]=1

  cnt=cnt+1
  if(cnt %% thelength==0){ #create a plot for each iteration of the input
    png(filename=paste0("plot_",plotnum,".png"))
    print(levelplot(mat))
    dev.off()
    plotnum=plotnum+1
  }
}

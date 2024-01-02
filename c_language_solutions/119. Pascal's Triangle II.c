int* getRow(int rowIndex, int* returnSize) {
   if(rowIndex<0){
       *returnSize =0;
       return NULL;
   }
   int** result = (int**)malloc((rowIndex+1)*sizeof(int*));
   *returnSize = rowIndex+1;
   for(int i = 0 ; i <= rowIndex;i++){
       result[i]=(int*)malloc((i+1)*sizeof(int));
       result[i][0]=1;
       result[i][i]=1;
       for(int j =1 ;j<i;j++){
           result[i][j]=result[i-1][j-1]+result[i-1][j];
       }
   }
   int* row = (int*)malloc((*returnSize)*sizeof(int));
   for(int i = 0 ;i< *returnSize;i++){
       row[i] = result[rowIndex][i];
   }
   for (int i = 0; i <= rowIndex; i++) {
        free(result[i]);
    }
    free(result);  
    return row;
}

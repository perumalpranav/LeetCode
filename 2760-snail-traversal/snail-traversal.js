/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    if (rowsCount * colsCount !== this.length) {
        return [];
    }

    let traversalGrid = []
    for (j = 0; j < rowsCount; j++) {
        let col = [];
        traversalGrid.push(col);
    }

    let thisIndex = 0
    for (i = 0; i < colsCount; i++){
        for (j = 0; j < rowsCount; j++) {
            if (i % 2 == 0) {
                traversalGrid[j].push(this[thisIndex]);
            }
            else {
                traversalGrid[rowsCount - (j + 1)].push(this[thisIndex]);
            }
            thisIndex += 1;
        }
    }

    return traversalGrid
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */
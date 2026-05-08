class DynamicArray {
    int[] elems;
    int size;
    int capacity;

    public DynamicArray(int capacity) {
        this.elems = new int[capacity];
        this.size = 0;
        this.capacity = capacity;
    }

    public int get(int i) {
        return this.elems[i];
    }

    public void set(int i, int n) {
        this.elems[i] = n;
    }

    public void pushback(int n) {
        
        int[] newElems = new int[this.size+1];
        for (int i = 0; i < this.size; i++) {
            newElems[i] = this.elems[i];
        }
        newElems[this.size] = n;
        this.elems = newElems;
        size += 1;
        if (this.size > this.capacity) {
            this.resize();
        }
    }

    public int popback() {
        int[] newElems = new int[this.size-1];
        int ret = this.elems[this.size-1];
        for (int i = 0; i < this.size-1; i++) {
            newElems[i] = this.elems[i];
        }
        this.elems = newElems;
        this.size -= 1;
        return ret;
    }

    private void resize() {
        int[] newElems = new int[this.size*2];
        for (int i = 0; i < this.size; i++) {
            newElems[i] = this.elems[i];
        }
        this.elems = newElems;
        this.capacity *= 2;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }
}

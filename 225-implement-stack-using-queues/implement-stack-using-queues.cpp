#include <queue>

class MyStack {
private:
    queue<int> q1, q2;

public:
    MyStack() {}
    
    void push(int x) {
        q2.push(x); //Q1: 3,2,1 Q2: 4
        while(!q1.empty()) {
            q2.push(q1.front()); // Q1:  Q2: 4,3,2,1
            q1.pop();
        }

        swap(q1,q2); // Q1: 4,3,2,1 Q2: 
    }
    
    int pop() {
        int temp = q1.front();
        q1.pop();
        return temp;
    }
    
    int top() {
        return q1.front();
    }
    
    bool empty() {
        return q1.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
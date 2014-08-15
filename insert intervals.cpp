// Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

// You may assume that the intervals were initially sorted according to their start times.

// Example 1:
// Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

// Example 2:
// Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

// This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
         vector<Interval> result;
         // consider the case where the input is ([],[5,7])
        if (intervals.empty()) {
            result.push_back(newInterval);
            return result;
        }
       
        bool first_time=true;
        for (int i=0;i<intervals.size();i++){
            //when the interval is before newInterval,push interval in result
            if (intervals[i].end<newInterval.start) result.push_back(intervals[i]);
            //when the interval is after NewInterval
            else if (intervals[i].start>newInterval.end) {
                // if newInterval hasn't put in result,push it in it
                if (first_time){
                result.push_back(newInterval);   
                first_time=false;
                    
                }
                result.push_back(intervals[i]);
            }
            //when the interval intersects new Interval,set the newInterval to contain the largest range
            else if (intervals[i].start<newInterval.start){
                newInterval.start=intervals[i].start;
                newInterval.end=newInterval.end>intervals[i].end?newInterval.end:intervals[i].end;
            }
            else if (intervals[i].end>newInterval.end){
                newInterval.end=intervals[i].end;
                newInterval.start=newInterval.start<intervals[i].start?newInterval.start:intervals[i].start;
                
                
            }
            
        }
        if (first_time) result.push_back(newInterval);
        return result;
        
    }
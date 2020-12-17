package com.oliverf.codewars;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;

public class Counter<T> extends HashMap {
    
    
    /* CONSTRUCTORS:
     *   - the 4 regular constructors inherited from HashMap
     *   - Counter(T[] arr)
     *   - Counter(Collection<T> coll)
     *   - Counter(Stream<T> stream)
     */
    public Map<T, Long> dict;
     
    Counter(T[] arr) {
        Map<T, Long> dict = new HashMap<T, Long>();
        for (T i : arr) {
            try {
                dict.put(i, dict.get(i) + 1);
            } catch (Exception ignored) {
                dict.put(i, 1L);
            }
            
        }
        System.out.println(dict);
    }
    
    Counter(Collection<T> coll) {
        
        Map<T, Long> dict = new HashMap<T, Long>();
        for (T i : coll) {
            try {
                dict.put(i, dict.get(i) + 1);
            } catch (Exception ignored) {
                dict.put(i, 1L);
            }
        }
    }
    
    Counter(Stream<T> stream) {
        Map<T, Long> dict = new HashMap<T, Long>();
        throw new UnsupportedOperationException();
    }
    
    
    /* STATIC BUILDERS:
     *     Counter.of(array), for all the primitive types:
     *          boolean[], byte[], char[], double[],
     *          float[],   int[],  long[], short[]
     *     Counter.of(String s), counting each letter as a String object.
     */
    
    
    
    /* OBSERVERS
     *
     *    Overrides needed:
     *      - toString:  being consistent with the requirements of the parent class
     *      - get:       providing the default value for non existing keys
     *
     *    New methods:
     *      - elements()            return a Stream with the elements duplicated according to their count
     *                              (keys are peeked in any order, but output all identical values together)
     *      - elementsAsList()      Same, but as list
     *
     *      - mostCommon()          Output a Stream of Map.Entry<T,Long> of the most common items (random order for equal counts)
     *      - mostCommon(n)         Same, but output only the n first entries
     *      - mostCommonAsList()
     *      - mostCommonAsList(n)
     */
    
    @Override
    public String toString() {
        return "Counter{" +
                "dict=" + dict +
                '}';
    }
    
    @Override
    public Object get(Object key) {
        return super.get(key);
    }
    
    
    /* MUTATORS
     *
     *  Non static versions:
     *    push(key)                         Add 1 to that key
     *    push(key, n)                      Add n to that key
     *
     *    pushAll(Collection<T> coll)       Add (and not "replace"!) all the contents of the array, map,...
     *    pushAll(T[] arr)                  to the current instance.
     *    pushAll(Stream<T> stream)
     *    pushAll(Map<T,Long> other)
     *
     *  Static versions:
     *    pushAll (Counter<Boolean>   cnt, boolean[] arr)
     *    pushAll (Counter<Byte>      cnt, byte[]    arr)
     *    pushAll (Counter<Character> cnt, char[]    arr)
     *    pushAll (Counter<Double>    cnt, double[]  arr)
     *    pushAll (Counter<Float>     cnt, float[]   arr)
     *    pushAll (Counter<Integer>   cnt, int[]     arr)
     *    pushAll (Counter<Long>      cnt, long[]    arr)
     *    pushAll (Counter<Short>     cnt, short[]   arr)
     *    pushAll (Counter<String>    cnt, String    s  )
     */
    
    
    
    /* MATHS OPERATIONS
     *  All these methods deliver a fresh Counter instance, where non positive values are suppressed.
     *  'a' and 'b' being Counter instances:
     *      a.add(b)            add all the counts together
     *      a.sub(b)            subtract counts of b from a.
     *      a.intersect(b)      keep the minimum
     *      a.union(b)          keep the max
     *
     *  Variations: those two will keep non positive values:
     *      a.subtract(b)       sub, but with non positive
     *      a.mul(n)            multiply all the values.
     */
    
    public Map<T, Long> add(Map<T, Long> b) {
        dict.forEach((k, v) -> b.merge(k, v, Long::sum));
        return dict;
    }
    
    // Sub
    
    public Map<T, Long> intersect(Map<T, Long> b) {
        dict.forEach((k, v) -> b.merge(k, v, Long::min));
        return dict;
    }
    
    public Map<T, Long> union(Map<T, Long> b) {
        dict.forEach((k, v) -> b.merge(k, v, Long::max));
        return dict;
    }

    
    
    public static void main(String[] args) {
        Integer[] arr = new Integer[]{1, 1, 3};
        Counter<Integer> test = new Counter<Integer>(arr);
        
        Integer[] arr2 = new Integer[]{1, 2, 3, 3, 3};
        Counter<Integer> test2 = new Counter<Integer>(arr2);
        //test.add(test2.dict);
        
        System.out.println(test.get(1));
        System.out.println(test.toString());
        
        //Collection<Integer> collTest = new Counter<Integer>(new Coll);
        
        
//        Stream<Integer> stream = Stream.of(1, 1, 2);
//        Counter<Integer> testStream = new Counter<Integer>(stream);
    }
    
}


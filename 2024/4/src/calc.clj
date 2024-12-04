(ns calc)

(defn rotate-90 [matrix]
  (mapv #(apply str %)
        (mapv reverse (apply mapv vector matrix))))

;; update to add padding in the left and right so the length of all odd rows are the same, and all even rows are the same
(defn rotate-45 [matrix]
  (mapv #(apply str %)
        (let [n (count matrix)
              m (count (first matrix))
              result (vec (repeat (+ n m -1) []))] ;; -1 since indices go from 0 to n+m-2
          (reduce
           (fn [res [i j]]
             (let [k (+ i j)]
               (assoc res k (conj (res k) (get-in matrix [i j])))))
           result
           (for [i (range n)
                 j (range m)]
             [j i])))))

(defn count-xmas-in-line [line]
  (+ (count (re-seq #"XMAS" line)) (count (re-seq #"SAMX" line))))

;; rotate 0 degrees (original), 45 degrees, 90 degrees, and 135 degrees
;; for each, find the word "XMAS" and "SAMX". count the total
(defn count-xmas [strings]
  (+
   (reduce + (map count-xmas-in-line strings))
   (reduce + (map count-xmas-in-line (rotate-90 strings)))
   (reduce + (map count-xmas-in-line (rotate-45 strings)))
   (reduce + (map count-xmas-in-line (rotate-45 (rotate-90 strings))))))

(defn count-x-mas [matrix]
  (let [n (count matrix)
        m (count (first matrix))
        result (atom 0)] ; Use atom to keep track of result
    (doseq [i (range 1 (dec n))
            j (range 1 (dec m))]
      (let [c (get-in matrix [i j])
            tl (get-in matrix [(dec i) (dec j)])
            tr (get-in matrix [(inc i) (dec j)])
            bl (get-in matrix [(dec i) (inc j)])
            br (get-in matrix [(inc i) (inc j)])]
        (when (and (= c \A)
                   (and (or (and (= tl \M) (= br \S)) (and (= tl \S) (= br \M)))
                        (or (and (= tr \M) (= bl \S)) (and (= tr \S) (= bl \M)))))
          (swap! result inc)))) ; Increment the atom result
    @result)) ; Dereference the atom to get the final value

(defn part-one [input]
  (count-xmas input))

(defn part-two [input]
  (count-x-mas input))

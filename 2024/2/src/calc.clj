(ns calc)

(defn monotonic? [arr]
  (let [sorted-arr (sort arr)]
    (or (= arr sorted-arr) (= arr (reverse sorted-arr)))))

(defn is-all-elements-diff-between [arr a b]
  (let [diffs (map abs (map #(apply - %) (partition 2 1 arr)))]
    (every? #(and (>= % a) (<= % b)) diffs)))

(defn satisfy-rules? [arr]
  (and (is-monotonic-array arr) (is-all-elements-diff-between arr 1 3)))

(defn part-one [matrix]
  (->> matrix
       (filter #(satisfy-rules? %))
       count))

(defn generate-possibilities [arr]
  (distinct
   (for [i (range (count arr))]
     (keep-indexed #(if (not= i %1) %2) arr))))

(defn part-two [matrix]
  (let [possibilities (map generate-possibilities matrix)]
    (->> possibilities
         (map #(some satisfy-rules? %))
         (keep identity)
         count)))

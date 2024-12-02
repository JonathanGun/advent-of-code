(ns calc)

(defn is-monotonic-array [arr]
  (let [sorted-arr (sort arr)]
    (or (= arr sorted-arr) (= arr (reverse sorted-arr)))))

(defn is-all-elements-diff-between [arr a b]
  (let [diffs (map #(apply - %) (partition 2 1 (reverse (sort arr))))]
    (every? #(and (>= % a) (<= % b)) diffs)))

(defn satisfies [arr]
  (and (is-monotonic-array arr) (is-all-elements-diff-between arr 1 3)))

(defn part-one [matrix]
  (->> matrix
       (filter #(satisfies %))
       count))

(defn generate-possibilities [arr]
  (distinct
   (for [i (range (count arr))]
     (vec (concat (subvec arr 0 i) (subvec arr (inc i)))))))

(defn part-two [matrix]
  (let [possibilities (map generate-possibilities matrix)]
    (->> possibilities
         (map #(some satisfies %))
         (keep identity)
         count)))

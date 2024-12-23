(ns calc)
(defn
 part-one
 [numbers]
 (let
  [odd
   (take-nth 2 numbers)
   even
   (take-nth 2 (rest numbers))
   sorted-odd
   (sort odd)
   sorted-even
   (sort even)
   result
   (reduce + (map abs (map - sorted-odd sorted-even)))]
  result))
(defn
 count-occurence
 [numbers]
 (reduce (fn [m n] (update m n (fnil inc 0))) (array-map) numbers))
(defn
 part-two
 [numbers]
 (let
  [odd
   (take-nth 2 numbers)
   even
   (take-nth 2 (rest numbers))
   count-odd
   (count-occurence odd)
   count-even
   (count-occurence even)
   result
   (reduce
    +
    (map (fn [[k v]] (* k v (get count-even k 0))) count-odd))]
  result))

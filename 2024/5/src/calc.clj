(ns calc
  (:require [clojure.set :as set]))

(defn process-rules [rules]
  (reduce (fn [result [k v]] (update result k (fnil conj #{}) v)) {} rules))

(defn satisfy-rules? [nums rules]
  (if (empty? nums) true
      (let [rule (get rules (first nums))
            rest_nums (set (rest nums))]
        (if (not-empty (set/difference rest_nums rule)) false
            (recur (rest nums) rules)))))

(defn get-middle [nums]
  (let [middle (int (/ (count nums) 2))]
    (nth nums middle)))

(defn filter-rules [rules current-instruction]
  (for [key current-instruction] [key (set/intersection (rules key) current-instruction)]))

(defn sort-by-value-length [m]
  (sort-by (fn [k] (count (m k))) (keys m)))

(defn get-rank [rules current-instruction]
  (->> current-instruction
       (filter-rules rules)
       (into {})
       (sort-by-value-length)))

(defn part-one [rules instructions]
  (->> instructions
       (filter #(satisfy-rules? % (process-rules rules)))
       (map get-middle)
       (reduce +)))

(defn part-two [rules instructions]
  (let [processed-rules (process-rules rules)]
    (->> instructions
         (filter #((complement satisfy-rules?) % processed-rules))
         (map #(get-rank processed-rules (set %)))
         (map get-middle)
         (reduce +))))

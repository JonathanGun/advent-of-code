(ns calc)

(defn part-one [input]
  (let [regex #"mul\((\d+),(\d+)\)"]
    (->> (re-seq regex input)
         (map #(* (Integer/parseInt (second %))
                  (Integer/parseInt (last %))))
         (reduce +))))

(defn part-two [input]
  (let [regex1 #"mul\((\d+),(\d+)\)"
        regex2 #"do\(\)|don't\(\)"
        input input
        matcher1 (re-matcher regex1 input)
        matcher2 (re-matcher regex2 input)]
    (loop [match1 (re-find matcher1)
           match2 (re-find matcher2)
           enabled? true
           result 0]
      (let [pos1 (when match1 (.start matcher1))
            pos2 (when match2 (.start matcher2))]
        (cond
          ;; Exit condition: no matches left
          (nil? match1)
          result

          ;; Process `match2` if it comes before `match1`
          (and pos2 (or (nil? pos1) (< pos2 pos1)))
          (let []
            ;; (println "changing do/dont to" (= match2 "do()"))
            (recur match1
                   (re-find matcher2)
                   (= match2 "do()")
                   result))

          ;; Process `match1` if it exists
          :else
          (let [product (* (Integer/parseInt (second match1))
                           (Integer/parseInt (last match1)))]
            ;; (if enabled? (println "adding to result" product) (println "skipping" product))
            (recur (re-find matcher1)
                   match2
                   enabled?
                   (if enabled? (+ result product) result))))))))

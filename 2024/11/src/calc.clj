(ns calc
  (:require [clojure.math :as math]
            [clojure.core.memoize :as memoize]))

(defn digits [num]
  (cond
    (zero? num) 0
    :else (+ 1 (digits (quot num 10)))))

(defn split [num d]
  (let [x (math/pow 10 (quot d 2))
        l (quot num x)
        r (rem num x)]
    [l r]))

(def step
  (memoize
   (fn [num s]
     (cond
       (zero? s) 1
       (zero? num) (step 1 (dec s))
       :else
       (let [d (digits num)
             [l r] (split num d)]
         (cond
           (even? d) (+ (step l (dec s)) (step r (dec s)))
           :else (step (* num 2024) (dec s))))))))

(defn part-one [input]
  (->> input
       (mapv #(step % 25))
       (reduce +)))

(defn part-two [input]
  (->> input
       (mapv #(step % 75))
       (reduce +)))

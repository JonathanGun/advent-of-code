(ns main
  (:require [calc]))

(defn -main
  [& args]
  (println (calc/part-one (slurp (first args))))
  (println (calc/part-two (slurp (first args)))))

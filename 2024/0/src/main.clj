(ns main
  (:require [calc]))

(defn -main
  [& args]
  (calc/part-one (slurp (first args)))
  (calc/part-two (slurp (first args))))

(ns main
  (:require [calc])
  (:require [util]))

(defn -main
  [& args]
  (println
   (calc/part-one
    (util/read-2d-vector (first args) #"\|")
    (util/read-2d-vector (second args) #",")))
  (println
   (calc/part-two
    (util/read-2d-vector (first args) #"\|")
    (util/read-2d-vector (second args) #","))))

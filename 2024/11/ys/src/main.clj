(ns main
  (:require [calc])
  (:require [util]))

(defn -main
  [& args]
  (println (calc/part-one (util/parse-file (first args))))
  (println (calc/part-two (util/parse-file (first args)))))

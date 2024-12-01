(ns main
  (:require [calc])
  (:require [clojure.string :as str]))


(defn parse-file [file-path]
  (-> file-path
      slurp
      (str/split #"\s+")
      (->> (map read-string))))

(defn -main
  [& args]
  (println (calc/part-one (parse-file (first args))))
  (println (calc/part-two (parse-file (first args)))))

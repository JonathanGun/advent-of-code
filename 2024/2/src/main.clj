(ns main
  (:require [calc])
  (:require [clojure.string :as str])
  (:require [clojure.java.io :as io]))

(defn read-2d-vector [file-path]
  (->> (slurp file-path)                                ;; Read the entire file content as a string
       (str/split-lines)                                ;; Split into lines
       (mapv (fn [line]                                 ;; For each line
               (mapv (fn [num] (Integer/parseInt num))  ;; For each number in the line
                     (str/split line #"\s+"))))))       ;; Split the line into numbers

(defn -main
  [& args]
  (println (calc/part-one (read-2d-vector (first args))))
  (println (calc/part-two (read-2d-vector (first args)))))

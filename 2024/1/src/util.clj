(ns util
  (:require [clojure.string :as str]))

(defn parse-file [file-path]
  (-> file-path
      slurp
      (str/split #"\s+")
      (->> (map read-string))))

(defn read-2d-vector [file-path]
  (->> (slurp file-path)                                ;; Read the entire file content as a string
       (str/split-lines)                                ;; Split into lines
       (mapv (fn [line]                                 ;; For each line
               (mapv (fn [num] (Integer/parseInt num))  ;; For each number in the line
                     (str/split line #"\s+"))))))       ;; Split the line into numbers

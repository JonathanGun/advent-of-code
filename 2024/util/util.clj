(ns util
  (:require [clojure.string :as str]))

(defn parse-file [file-path & [delim]]
  (-> file-path
      slurp
      (str/split (or delim #"\s+"))
      (->> (map read-string))))

(defn read-2d-vector [file-path & [delim]]
  (->> (slurp file-path)                                     ;; Read the entire file content as a string
       (str/split-lines)                                     ;; Split into lines
       (mapv (fn [line]                                      ;; For each line
               (mapv (fn [num] (Integer/parseInt num))       ;; For each number in the line
                     (str/split line (or delim #"\s+"))))))) ;; Split the line into numbers

(defn read-2d-string [file-path]
  (->> (slurp file-path)                                ;; Read the entire file content as a string
       (str/split-lines)))                              ;; Split into lines

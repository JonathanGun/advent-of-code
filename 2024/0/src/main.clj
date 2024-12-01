(ns main
  (:require [calc])
  (:require [clojure.string :as str]))


;; (defn parse-file [file-path]
;;   (-> file-path
;;       slurp
;;       (str/split #"\s+")
;;       (->> (map read-string))))

(defn -main
  [& args]
  (println "Hello, World!" args))

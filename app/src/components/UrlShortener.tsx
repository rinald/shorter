import { useRef } from "react";
import styles from "../styles/shortener.module.css";

import { createShortUrl } from "../util/api";

const UrlShortener = () => {
  const inputRef = useRef<HTMLInputElement | null>(null);

  return (
    <form
      className={styles.urlShortener}
      onSubmit={(e) => {
        e.preventDefault();
        createShortUrl(inputRef.current!.value);
      }}
    >
      <input
        type="url"
        name="long-url"
        pattern="https://.*"
        ref={inputRef}
        className={styles.input}
        placeholder="Enter the url you want to shorten"
      />
      <button id="shorten-url" className={styles.button}>
        Shorten URL
      </button>
    </form>
  );
};

export default UrlShortener;

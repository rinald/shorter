import { useRef, useTransition, useState } from "react";

import styles from "../styles/shortener.module.css";
import { createShortUrl } from "../util/api";

type Props = {
  hash: string;
  long_url: string;
};

const ShortUrl = ({ hash, long_url }: Props) => {
  return (
    <ul className={styles.shortUrl}>
      <li>
        Short url:{" "}
        <a
          href={`http://localhost:8000/url/${hash}`}
        >{`http://localhost:8000/${hash}`}</a>
      </li>
      <li>
        Long url: <a href={long_url}>{long_url}</a>
      </li>
    </ul>
  );
};

const UrlShortener = () => {
  const inputRef = useRef<HTMLInputElement | null>(null);
  const [isPending, startTransition] = useTransition();
  const [shortUrl, setShortUrl] = useState<any>(null);

  return !shortUrl ? (
    <form
      className={styles.urlShortener}
      onSubmit={(e) => {
        e.preventDefault();
        startTransition(async () => {
          try {
            const data = await createShortUrl(inputRef.current!.value);
            setShortUrl(data);
          } catch (error) {
            console.error(error);
          }
        });
      }}
      aria-disabled={isPending}
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
  ) : (
    <ShortUrl hash={shortUrl.hash} long_url={shortUrl.long_url} />
  );
};

export default UrlShortener;

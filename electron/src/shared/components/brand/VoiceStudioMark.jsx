import React from 'react';

/**
 * PakThai Studio's compact mark: a microphone.
 * The desktop icon uses the same silhouette on a dark tile; app chrome keeps
 * it transparent so it stays crisp at titlebar sizes and in every theme.
 */
export default function VoiceStudioMark({ className = '', title, ...props }) {
  return (
    <svg
      viewBox="0 0 64 64"
      fill="none"
      className={className}
      role={title ? 'img' : undefined}
      aria-hidden={title ? undefined : true}
      {...props}
    >
      {title ? <title>{title}</title> : null}
      <rect x="23" y="8" width="18" height="28" rx="9" fill="currentColor" />
      <path
        d="M14 29c0 9.9 8.1 18 18 18s18-8.1 18-18M32 47v9M23 57h18"
        stroke="currentColor"
        strokeWidth="5.5"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}

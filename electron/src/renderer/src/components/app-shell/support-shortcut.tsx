import './support-shortcut.css';
import { GithubStar } from './github-star';

// PakThai Studio: the upstream "Get Pro" upsell is not shown in the header;
// only the star link crediting the upstream VoiceStudio project remains.
export function SupportShortcut() {
  return (
    <div className="flex shrink-0 items-center gap-0.5">
      <GithubStar />
    </div>
  );
}

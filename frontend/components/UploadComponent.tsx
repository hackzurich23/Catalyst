import { AccessibilityChoice } from "./AccessibilityChoice";
import { Dropzone } from "./DropZone";

export const UploadComponent = () => {
	return (
		<section className="section">
			<Dropzone />
			<AccessibilityChoice />
		</section>
	);
};

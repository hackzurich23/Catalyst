import FetchApiComponent from "@/components/FetchApiComponent";
import { Layout } from "@/components/Layout";
import { UploadComponent } from "@/components/UploadComponent";

export default function Upload() {
	return (
		<Layout>
			<UploadComponent />
			<FetchApiComponent />
		</Layout>
	);
}

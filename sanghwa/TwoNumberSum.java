import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class TwoNumberSum {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int[] arr = new int[st.countToken()];
		int idx = 0;

		Set<Integer> set = new HashSet<>();

		while (st.hasMoreToken()) {
			arr[idx++] = Integer.parseInt(st.nextToken());
		}

		for (int i = 0; i < arr.length - 1; i++) {
			for (int j = i + 1; j < arr.length; j++) {
				set.add(arr[i] + arr[j]);
			}
		}

		int[] result = set.stream().sorted().mapToInt(Integer::intValue).toArray();
		System.out.println(Arrays.toString(result));
	}
}

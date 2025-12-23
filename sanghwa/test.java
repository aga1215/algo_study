public class test{
	public static void main(String[] args) IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int[] answer = new int[st.countTokens()];
		int idx = 0;
		while (st.hasMoreTokens()) {
			answer[idx++] = Integer.parseInt(st.nextToken());
		}

		int[] student1 = {1, 2, 3, 4, 5};
		int[] student2 = {2, 1, 2, 3, 2, 4, 2, 5};
		int[] student3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

		int c1 = 0, c2 = 0, c3 = 0;
		for (int i = 0; i < answer.length; i++) {
			if (answer[i] == student1[i % student1.length])
				c1++;
			if (answer[i] == student2[i % student2.length])
				c2++;
			if (answer[i] == student3[i % student3.length])
				c3++;
		}

		int max = Math.max(c1, Math.max(c2, c3));
		List<Integer> winner = new ArrayList<>();
		if (c1 == max)
			winner.add(1);
		if (c2 == max)
			winner.add(2);
		if (c3 == max)
			winner.add(3);

		int[] result = winner.stream().sorted().mapToInt(Integer::intValue).toArray();
		System.out.println(Arrays.toString(result));
	}
}
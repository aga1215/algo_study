import java.io.*;
import java.util.*;

public class MatrixMultifly {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		int r1 = Integer.parseInt(st.nextToken());
		int c1 = Integer.parseInt(st.nextToken());

		int[][] A = new int[r1][c1];
		for (int i = 0; i < r1; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < c1; j++) {
				A[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		st = new StringTokenizer(br.readLine());
		int r2 = Integer.parseInt(st.nextToken());
		int c2 = Integer.parseInt(st.nextToken());

		int[][] B = new int[r2][c2];
		for (int i = 0; i < r2; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < c2; j++) {
				B[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int[][] result = new int[r1][c2];

		for (int i = 0; i < r1; i++) {
			for (int j = 0; j < c2; j++) {
				for (int k = 0; k < c1; k++) {
					result[i][j] += A[i][k] * B[k][j];
				}
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < r1; i++) {
			for (int j = 0; j < c2; j++) {
				sb.append(result[i][j]).append(" ");
			}
			sb.append("\n");
		}
		System.out.print(sb.toString());
	}
}

import java.util.*;
import java.io.*;

public class Main {
	static class Pos {
		int x, y, d;

		public Pos(int x, int y, int d) {
			this.x = x;
			this.y = y;
			this.d = d;
		}
	}
	
	static int n, m;
	static int[][] map;
	static int[][] dir = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};	
	static Pos robot;
	static int ans = 1;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		map = new int[n][m];
		
		st = new StringTokenizer(br.readLine());
		int xx = Integer.parseInt(st.nextToken());
		int yy = Integer.parseInt(st.nextToken());
		int dd = Integer.parseInt(st.nextToken());
		
		robot = new Pos(xx, yy, dd);
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		clean(robot);
		System.out.println(ans);
	}

	private static void clean(Pos robot) {
		int now_x = robot.x;
		int now_y = robot.y;
		int now_d = robot.d % 4;
		
		map[now_x][now_y] = 2;
		
		while(true) {
			
//			for(int i = 0; i < n; i++) {
//				for(int j = 0; j < m; j++) {
//					System.out.printf("%d ", map[i][j]);
//				} System.out.println();
//			} System.out.println("----------------------------");
			
			// 북 서 남 동
			// 0 3 2 1
			for(int i = 1; i <= 5; i++) {
				int nd = Math.abs(now_d + 3) % 4;
				int nx = now_x + dir[nd][0];
				int ny = now_y + dir[nd][1];
				
				if(i == 5) {
					now_x = now_x - dir[now_d][0];
					now_y = now_y - dir[now_d][1];
					
					if(!inRange(now_x, now_y)) return;
					break;
				}
				
				if(inRange(nx, ny) && map[nx][ny] == 0) {
					map[nx][ny] = 2;
					now_x = nx;
					now_y = ny;
					now_d = nd;
					ans += 1;
					break;
				}
				
				if(map[nx][ny] != 0) {
					now_d = nd;
					continue;
				}				
			}			
			
		}
	}

	private static boolean inRange(int nx, int ny) {
		if(nx < 0 || nx >= n || ny < 0 || ny >= m || map[nx][ny] == 1) return false;
		else return true;
	}

}

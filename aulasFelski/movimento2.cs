using Godot;
using System;

public partial class jogador : Area2D {
	private int area_quadrado = 64;
	private Vector2 direcao;
	private RayCast2D ray;
	public override void _Ready() {
		ray = GetNode<RayCast2D>("RayCast2D");
	}
	public void Movimento() {
		//detecta a direção desejada
		if (Input.IsActionJustPressed("cima")) {
			direcao = new Vector2(0,-1);
		}
		if (Input.IsActionJustPressed("baixo")) {
			direcao = new Vector2(0, 1);
		}
		if (Input.IsActionJustPressed("esquerda")) {
			direcao = new Vector2(-1, 0);
		}
		if (Input.IsActionJustPressed("direita")) {
			direcao = new Vector2(1, 0);
		}
		
		ray.TargetPosition = direcao * area_quadrado;
		ray.ForceRaycastUpdate();
		if (!ray.IsColliding()) {
			Position += direcao * area_quadrado;
		} else {
			if (ray.GetCollider() is Area2D) {
				GD.Print("Área2D está bloqueando o caminho");
			}
		}
			
		
	}
	public override void _UnhandledInput(InputEvent @event) {
		if (@event is InputEventKey eventKey)
			if (eventKey.Pressed)
				Movimento();
	}
	
}
using Godot;
using System;

public partial class Sprite2D : Godot.Sprite2D {
	// Called when the node enters the scene tree for the first time.
	public override void _Ready() {
		GlobalPosition = new Vector2(100, 100);
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta) {
		if (Input.IsActionPressed("direita") && GlobalPosition.X < 1024) {
			GlobalPosition = GlobalPosition + new Vector2(1,0);
		}
		if (Input.IsActionPressed("esquerda") && GlobalPosition.X > 64) {
			GlobalPosition = GlobalPosition + new Vector2(-1,0);
		}
		if (Input.IsActionPressed("cima") && GlobalPosition.Y > 64) {
			GlobalPosition = GlobalPosition + new Vector2(0,-1);
		}
		if (Input.IsActionPressed("baixo") && GlobalPosition.Y < 512) {
			GlobalPosition = GlobalPosition + new Vector2(0,1);
		}
	}
}
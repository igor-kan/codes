; ModuleID = 'algorithms/02_c/graphs/bfs.c'
source_filename = "algorithms/02_c/graphs/bfs.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [4 x i8] c"%d \00", align 1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local void @bfs(ptr noundef readonly captures(none) %0, i32 noundef %1, i32 noundef %2) local_unnamed_addr #0 {
  %4 = alloca [100 x i32], align 16
  %5 = alloca [100 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %4) #4
  call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(400) %4, i8 0, i64 400, i1 false)
  call void @llvm.lifetime.start.p0(ptr nonnull %5) #4
  %6 = sext i32 %2 to i64
  %7 = getelementptr inbounds i32, ptr %4, i64 %6
  store i32 1, ptr %7, align 4, !tbaa !5
  store i32 %2, ptr %5, align 16, !tbaa !5
  %8 = icmp sgt i32 %1, 0
  %9 = zext nneg i32 %1 to i64
  br label %14

10:                                               ; preds = %39, %14
  %11 = phi i32 [ %16, %14 ], [ %40, %39 ]
  %12 = sext i32 %11 to i64
  %13 = icmp slt i64 %17, %12
  br i1 %13, label %14, label %43, !llvm.loop !9

14:                                               ; preds = %3, %10
  %15 = phi i64 [ 0, %3 ], [ %17, %10 ]
  %16 = phi i32 [ 1, %3 ], [ %11, %10 ]
  %17 = add nuw nsw i64 %15, 1
  %18 = getelementptr inbounds nuw i32, ptr %5, i64 %15
  %19 = load i32, ptr %18, align 4, !tbaa !5
  %20 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %19)
  br i1 %8, label %21, label %10

21:                                               ; preds = %14
  %22 = sext i32 %19 to i64
  %23 = getelementptr inbounds [100 x i32], ptr %0, i64 %22
  br label %24

24:                                               ; preds = %21, %39
  %25 = phi i64 [ 0, %21 ], [ %41, %39 ]
  %26 = phi i32 [ %16, %21 ], [ %40, %39 ]
  %27 = getelementptr inbounds nuw i32, ptr %23, i64 %25
  %28 = load i32, ptr %27, align 4, !tbaa !5
  %29 = icmp eq i32 %28, 0
  br i1 %29, label %39, label %30

30:                                               ; preds = %24
  %31 = getelementptr inbounds nuw i32, ptr %4, i64 %25
  %32 = load i32, ptr %31, align 4, !tbaa !5
  %33 = icmp eq i32 %32, 0
  br i1 %33, label %34, label %39

34:                                               ; preds = %30
  store i32 1, ptr %31, align 4, !tbaa !5
  %35 = add nsw i32 %26, 1
  %36 = sext i32 %26 to i64
  %37 = getelementptr inbounds i32, ptr %5, i64 %36
  %38 = trunc nuw nsw i64 %25 to i32
  store i32 %38, ptr %37, align 4, !tbaa !5
  br label %39

39:                                               ; preds = %24, %30, %34
  %40 = phi i32 [ %26, %30 ], [ %35, %34 ], [ %26, %24 ]
  %41 = add nuw nsw i64 %25, 1
  %42 = icmp eq i64 %41, %9
  br i1 %42, label %10, label %24, !llvm.loop !11

43:                                               ; preds = %10
  call void @llvm.lifetime.end.p0(ptr nonnull %5) #4
  call void @llvm.lifetime.end.p0(ptr nonnull %4) #4
  ret void
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: write)
declare void @llvm.memset.p0.i64(ptr writeonly captures(none), i8, i64, i1 immarg) #2

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #3

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

attributes #0 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: write) }
attributes #3 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
!11 = distinct !{!11, !10}
